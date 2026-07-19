
def generate_summary_report(history : list):
    print(f"\n{'File':<25} {'Extension':<15} {'Destination':<20} {'Status':<10} {'Timestamp':<20}")
    print("-" * 85)

    for row in history:
        print(f"{row['file']:<25} {row['extension']:<15} {row['destination']:<20} {row['status']:<10} {row['timestamp']:<20}")
    