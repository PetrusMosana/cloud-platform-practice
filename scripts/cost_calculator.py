import json
import sys

CPU_COST = 10
MEMORY_COST = 5


def fail(message):
    print("FAIL")
    print(message)
    sys.exit(1)


def calculate_resource_cost(resource):
    name = resource.get("name")
    cpu = resource.get("cpu")
    memory = resource.get("memory")

    if not name:
        fail("Resource is missing a name")

    if not isinstance(cpu, int) or cpu < 1 or cpu > 16:
        fail(f"{name} has invalid CPU value: {cpu}")

    if not isinstance(memory, int) or memory < 1 or memory > 64:
        fail(f"{name} has invalid memory value: {memory}")

    return (cpu * CPU_COST) + (memory * MEMORY_COST)


def main():
    with open("resources.json", "r") as file:
        resources = json.load(file)

    total = 0

    for resource in resources:
        cost = calculate_resource_cost(resource)
        total += cost
        print(f"{resource['name']} = ${cost}")

    print(f"\nTotal = ${total}")


if __name__ == "__main__":
    main()