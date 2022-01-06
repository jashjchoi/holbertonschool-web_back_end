const assert = require('assert');
const calculateNumber = require('./1-calcul');

// describe('calculateNumber', function () {
//   describe('Integers', function () {
//     it('return 4', function () {
//       assert.strictEqual(calculateNumber(1, 3), 4);
//     });
//   });

//   describe('1st rounded', function () {
//     it('return 5', function () {
//       assert.strictEqual(calculateNumber(1, 3.7), 5);
//     });
//   });

//    describe('One float', function () {
//     it('return 5', function () {
//       assert.strictEqual(calculateNumber(3.7, 1), 5);
//     });
//   });

//     describe('2nd rounded', function () {
//     it('return 5', function () {
//       assert.strictEqual(calculateNumber(1, 5.2), 6);
//     });
//   });

//   describe('Two floats', function () {
//     it('return 5', function () {
//       assert.strictEqual(calculateNumber(1.2, 3.7), 5);
//     });
//   });
// });

describe('SUM', () => {
  it('return rounded number', () => {
    assert.strictEqual(calculateNumber('SUM', 4, 3), 7);
    assert.strictEqual(calculateNumber('SUM', 1.8, 0), 2);
    assert.strictEqual(calculateNumber('SUM', 5.1, 3.1), 8);
  });
});

describe('SUBTRACT', () => {
  it('return rounded number', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 4, 3), 1);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.8, 0), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', 5.1, 3.1), 2);
  });
});

describe('DIVIDE', () => {
  it('returns rounded positive divide', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 6, 2), 3);
    assert.strictEqual(calculateNumber('DIVIDE', 6.1, 1.8), 3);
    assert.strictEqual(calculateNumber('DIVIDE', 4.9, 5), 1);
  });
  it('returns Error', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1, 0), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 3, 0), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 6, 0), 'Error');
  });
});
