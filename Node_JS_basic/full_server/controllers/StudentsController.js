const readDatabase = require('../utils');

const DB_FILE = process.argv.find((arg) => arg.endsWith('.csv'));

class StudentsController {
  static getAllStudents(req, res) {
    readDatabase(DB_FILE)
      .then((fields) => {
        const output = ['This is the list of our students'];

        const sortedFields = Object.keys(fields).sort((a, b) => (
          a.toLowerCase().localeCompare(b.toLowerCase())
        ));

        sortedFields.forEach((field) => {
          const list = fields[field];
          output.push(
            `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`
          );
        });

        res.status(200).send(output.join('\n'));
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(DB_FILE)
      .then((fields) => {
        const list = fields[major] || [];
        res.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

module.exports = StudentsController;
