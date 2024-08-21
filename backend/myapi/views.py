from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# In-memory storage for tasks
tasks = []

# GET endpoint to retrieve all tasks
def get_tasks(request):
    return JsonResponse(tasks, safe=False)

# POST endpoint to add a new task
@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        try:
            # Log raw request body
            print(f"Raw request body: {request.body}")

            # Parse the request body
            data = json.loads(request.body)

            # Log parsed data to ensure correct data is being received
            print(f"Parsed request data: {data}")

            # Construct the task
            task = {
                "id": len(tasks) + 1,  # Simple ID assignment
                "title": data.get('title', ''),  # Using .get() to handle missing fields
                "description": data.get('description', ''),
            }

            # Log task creation
            print(f"Task created: {task}")

            # Add task to the list
            tasks.append(task)

            return JsonResponse(task, status=201)

        except json.JSONDecodeError:
            # Log decoding error
            print("Error: Invalid JSON format")
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except KeyError as e:
            # Log missing key error
            print(f"Error: Missing key {str(e)}")
            return JsonResponse({"error": f"Missing key: {str(e)}"}, status=400)

    # Log when method is not allowed
    print("Error: Method not allowed")
    return JsonResponse({"error": "Method Not Allowed"}, status=405)
