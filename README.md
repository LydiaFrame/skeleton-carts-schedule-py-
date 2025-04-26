# skeleton-carts-schedule-py-
This is a simple scheduling program that assigns grocery store baggers to cart retrieval shifts throughout the day.

# Cart Assignment Scheduler

This is a simple scheduling program that assigns grocery store baggers to cart retrieval shifts throughout the day.

## 📋 Features

- Input baggers' names and their shift times
- Automatically generate cart assignments from **7:00 AM to 10:00 PM**
- Assignments are in **30-minute increments**
- Ensures baggers are **not assigned back-to-back cart runs**

## 🛠 How to Run

1. Open a terminal.
2. Run `main.py`:

3. Follow the prompts to enter bagger names and work hours.

## Example Input
Enter number of baggers: 2
Enter bagger name: Lydia
Enter start time (HH:MM, 24-hour): 07:00
Enter end time (HH:MM, 24-hour): 11:00

Enter bagger name: Sam
Enter start time (HH:MM, 24-hour): 08:00
Enter end time (HH:MM, 24-hour): 12:00

## Output
- A list of all cart assignments for the day
- An "UpNext" display showing who’s first on the schedule

Schedule uploaded successfully.
Schedule validated.

Generating cart assignments...

Generated Cart Assignments:
07:00 - 07:30 → Lydia
07:30 - 08:00 → Sam
08:00 - 08:30 → Lydia
08:30 - 09:00 → Sam
09:00 - 09:30 → Lydia
09:30 - 10:00 → Sam
10:00 - 10:30 → Lydia
10:30 - 11:00 → Sam
11:00 - 11:30 → Sam

Up Next:
07:00 - 07:30 → Lydia

