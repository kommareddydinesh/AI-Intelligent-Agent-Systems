
# =====================================================
# SMART MUSEUM ARTIFACT PROTECTION SYSTEM
# Model-Based Reflex Agent
# =====================================================

from datetime import datetime

# Security Configuration
SAFE_DISTANCE = 100
RESTRICTED_DISTANCE = 50

# Internal State (Memory)
internal_state = {
    "warning_given": False,
    "alarm_active": False,
    "violation_count": 0,
    "total_readings": 0,
    "event_log": []
}


# Function to Apply Model-Based Rules
def apply_model_based_rules(distance):

    warning_before = internal_state["warning_given"]
    internal_state["total_readings"] += 1

    if distance < RESTRICTED_DISTANCE:
        internal_state["violation_count"] += 1

        if not warning_before:
            matched_rule = "First restricted-zone violation"
            action = "Display Warning Message"
            result = "Please stay away from the artifact."

            internal_state["warning_given"] = True
            internal_state["alarm_active"] = False

        else:
            matched_rule = "Visitor ignored previous warning"
            action = "Activate Security Alarm"
            result = "Security Alert! Visitor is too close."

            internal_state["alarm_active"] = True

    elif distance < SAFE_DISTANCE:
        matched_rule = "Visitor entered caution zone"
        action = "Display Caution Message"
        result = "Caution! Please maintain a safe distance."

        internal_state["alarm_active"] = False

    else:
        matched_rule = "Visitor is at a safe distance"
        action = "Continue Monitoring"
        result = "Safe distance. Artifact is protected."

        internal_state["warning_given"] = False
        internal_state["alarm_active"] = False

    warning_after = internal_state["warning_given"]

    # Record the event
    internal_state["event_log"].append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "distance": distance,
        "rule": matched_rule,
        "action": action
    })

    return (
        matched_rule,
        action,
        result,
        warning_before,
        warning_after,
        internal_state["alarm_active"]
    )


# Alarm Function
def activate_alarm():
    print("\n" + "!" * 45)
    print("   SECURITY ALARM ACTIVATED!")
    print("   Protect the artifact immediately!")
    print("!" * 45)


# Display Dashboard
def display_dashboard(
    distance, rule, action, result,
    warning_before, warning_after, alarm
):

    if distance >= SAFE_DISTANCE:
        zone = "SAFE"
    elif distance >= RESTRICTED_DISTANCE:
        zone = "CAUTION"
    else:
        zone = "RESTRICTED"

    print("\n" + "=" * 50)
    print("          MUSEUM SECURITY REPORT")
    print("=" * 50)

    print(f"Date and Time       : {datetime.now():%Y-%m-%d %H:%M:%S}")
    print(f"Visitor Distance    : {distance:.2f} cm")
    print(f"Security Zone       : {zone}")
    print(f"Memory Before       : {warning_before}")
    print(f"Matched Rule        : {rule}")
    print(f"Action              : {action}")
    print(f"Memory After        : {warning_after}")
    print(f"Alarm Status        : {'ACTIVE' if alarm else 'INACTIVE'}")
    print(f"Total Readings      : {internal_state['total_readings']}")
    print(f"Recorded Violations : {internal_state['violation_count']}")
    print(f"Result              : {result}")

    print("=" * 50)


# Main Function: Accept Only One Input
def run_monitor():

    print("=" * 50)
    print(" SMART MUSEUM ARTIFACT PROTECTION SYSTEM")
    print("      Model-Based Reflex Agent")
    print("=" * 50)

    print(f"Safe Zone       : {SAFE_DISTANCE} cm and above")
    print(f"Caution Zone    : {RESTRICTED_DISTANCE} to {SAFE_DISTANCE} cm")
    print(f"Restricted Zone : Below {RESTRICTED_DISTANCE} cm")

    try:
        distance = float(input("\nEnter Visitor Distance (cm): "))

        if distance < 0:
            print("Error: Distance cannot be negative.")
            return

        (
            rule,
            action,
            result,
            before,
            after,
            alarm
        ) = apply_model_based_rules(distance)

        display_dashboard(
            distance,
            rule,
            action,
            result,
            before,
            after,
            alarm
        )

        if alarm:
            activate_alarm()

    except ValueError:
        print("Invalid input! Please enter a valid number.")

    finally:
        print("\nMonitoring stopped. Program ended.")


# Program Execution
if __name__ == "__main__":
    run_monitor()
