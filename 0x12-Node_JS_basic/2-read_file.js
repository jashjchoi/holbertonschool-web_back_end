const fs = require('fs');

module.exports = function countStudents(path) {
  try {
    let data = fs.readFileSync(path, 'utf8').toString().split('\n');
    data = data.slice(1, data.length - 1);
    console.log(`Number of students: ${data.length}`);

    const arr = {};
    data.forEach((item) => {
      const student = item.split(',');
      if (!arr[student[3]]) arr[student[3]] = [];
      arr[student[3]].push(student[0]);
    });

    for (const key in arr) {
      if (key) {
        console.log(`Number of students in ${key}: ${arr[key].length}. List: ${arr[key].join(', ')}`);
      }
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};
