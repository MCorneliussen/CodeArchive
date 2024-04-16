const fs = require('fs');
const path = require('path');

function convertToJsonWithSql(inputFileName, outputFileName, tableName) {
    const rawDataFilePath = path.join(__dirname, '..', 'public', 'json', inputFileName);
    const data = JSON.parse(fs.readFileSync(rawDataFilePath, 'utf-8'));

    const queries = data.map(item => {
        const columns = Object.keys(item).join(', ');
        const values = Object.values(item).map(value =>
            typeof value === 'boolean' ? (value ? 'TRUE' : 'FALSE') : 
            typeof value === 'string' ? `'${value.replace("'", "''")}'` : value 
            ).join(', ');
            return {
                query: `INSERT INTO ${tableName} (${columns}) VALUES (${values});`
            };
    });

    const outputFilePath = path.join(__dirname, '..', 'public', 'json', outputFileName);


    fs.writeFileSync(outputFilePath, JSON.stringify(queries, null, 2), 'utf-8');
    console.log(`Converted JSON with SQL queries saved to ${outputFileName}`);
}

convertToJsonWithSql('animals.json', 'animalsWithSql.json', 'Animals');
convertToJsonWithSql('users.json', 'usersWithSql.json', 'Users');
