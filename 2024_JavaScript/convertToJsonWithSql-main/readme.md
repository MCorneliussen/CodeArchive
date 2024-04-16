### Instructions for Use

**Converting JSON Data to SQL Queries**

This script transforms raw JSON data into SQL insert queries and saves them in a new JSON file for easy database population.

**Requirements:**
- Node.js installed on your system.
- Input JSON files placed in the `public/json` directory of your project.

**Usage:**
1. Place your input JSON files (e.g., `animals.json`, `users.json`) in the `public/json` directory.
2. Ensure the script `convertToJsonWithSql.js` is located appropriately in your project so that the relative path to the `public/json` directory is correct.
3. Run the script using Node.js from your terminal:

```bash
node path/to/convertToJsonWithSql.js
```

Replace `path/to/` with the actual path to where your script is located.

**Input Files:**
- `animals.json`
- `users.json`

These files should contain an array of objects, where each object represents a record to be inserted into the database.

**Output Files:**
- `animalsWithSql.json`
- `usersWithSql.json`

The script generates these output files containing SQL insert queries based on the data from the input files. Yes, `.json` should be included in the `outputFileName` argument to ensure the output is saved with the correct file extension.

**Function Call:**
- The script is called directly from the command line as shown above. It automatically processes the specified input files and generates output files with SQL queries.
- Make sure to update the function calls at the bottom of the script if you have different tables or file names.

This guide should help you understand and utilize the script effectively for converting JSON data into SQL queries for database population.