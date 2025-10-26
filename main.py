import statistics
from collections import defaultdict

# --- DATA ---
employees = [
    {"name": "Alice", "department": "Sales", "scores": [80, 85, 90]},
    {"name": "Bob", "department": "IT", "scores": [70, 75, 72]},
    {"name": "Charlie", "department": "Sales", "scores": [88, 92, 85]},
    {"name": "David", "department": "IT", "scores": [95, 90, 93]},
    {"name": "Eve", "department": "HR", "scores": [90, 85, 88]},
    {"name": "Frank", "department": "Sales", "scores": [75, 80, 70]},
    {"name": "Grace", "department": "Marketing", "scores": [82, 83, 84]},
    {"name": "Heidi", "department": "IT", "scores": [65, 70, 68]},
]

# --- FUNCTIONS ---

def get_department_stats(employee_data):
    """
    Groups all scores by department and calculates the average and highest score
    for each department. Returns a tuple: (department_averages, department_highest)
    """
    department_scores = defaultdict(list)
    for employee_stat in employee_data:
        department_scores[employee_stat["department"]].extend(employee_stat["scores"])

    department_averages = {}
    department_highest = {}

    for department, scores in department_scores.items():
        # Calculate Average
        department_averages[department] = statistics.mean(scores)
        # Calculate Highest
        department_highest[department] = max(scores)

    return department_averages, department_highest


def warning_list(employee_data, threshold):
    """
    Identifies employees whose individual average score is below the given threshold.
    Returns a list of dictionaries.
    """
    warning_employees = []

    for employee_to_warn in employee_data:
        # Calculate the employee's individual average score
        employee_avg = statistics.mean(employee_to_warn["scores"])

        # Check if the average is below the threshold
        if employee_avg < threshold:
            warning_employees.append({
                "name": employee_to_warn["name"],
                "department": employee_to_warn["department"],
                "average_score": employee_avg
            })

    return warning_employees


# --- EXECUTION ---

# Set the threshold for the warning list
PASSING_THRESHOLD = 85

# Get the department statistics
avg_scores_by_dept, highest_scores_by_dept = get_department_stats(employees)

# Get the list of employees below the threshold
employees_to_warn = warning_list(employees, PASSING_THRESHOLD)

# --- PRINT RESULTS ---

print("=" * 40)
print("  EMPLOYEE PERFORMANCE ANALYSIS")
print("=" * 40)

print("\n--- Department Statistics ---")

print("\nAverage Score Per Department:")
for dept, avg in avg_scores_by_dept.items():
    print(f"  📊 {dept}: {avg:.2f}")

print("\nHighest Score Per Department:")
for dept, high in highest_scores_by_dept.items():
    print(f"  🏆 {dept}: {high:.2f}")

print(f"\n--- Warning List (Individual Avg. Below {PASSING_THRESHOLD}) ---")
if employees_to_warn:
    for employee in employees_to_warn:
        print(f"  🚨 {employee['name']} ({employee['department']}) - Avg: {employee['average_score']:.2f}")
else:
    print("  🎉 No employees are below the threshold!")

print("=" * 40)