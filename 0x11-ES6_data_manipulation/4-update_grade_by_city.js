export default function updateStudentGradeByCity(students, city, newGrades) {
  const update = (arg) => {
    const student = arg;
    const grade = newGrades.filter((item) => item.studentId === student.id)[0];
    if (grade) student.grade = grade.grade;
    else student.grade = 'N/A';
    return student;
  };

  const newArray = students.map(update);
  return newArray.filter((student) => student.location === city);
}
