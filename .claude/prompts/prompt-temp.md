# Context

- The last update to the date string in the daily-spread-table header-rows needs some fixes.

# Instruction

1. We need to include the month name in the string.
   - Example(s)
     - "January 1st,  2026-01-01,  Week 1"

2. Remember to leave two spaces after the commas.
   ```txt
   "Thursday 1st,  2026-01-01,  (Week 1)"
    .............↑↑...........↑↑........
             Two-spaces   Two-spaces    
   ```

3. While we are here fixing these bugs, may as well through in a new requirement while we're at it. So, remove the brakets around the week. 
   - Example(s)
     - "Thursday 1st,  2026-01-01  Week 1"
     - "Tuesday 27th,  2026-01-27,  Week 4"
     - "December 31st,  2026-12-31, Week 52"
