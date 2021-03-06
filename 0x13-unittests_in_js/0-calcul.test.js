const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  describe('Integers', function () {
    it('return 4', function () {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });
  });

  describe('1st rounded', function () {
    it('return 5', function () {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
  });

   describe('One float', function () {
    it('return 5', function () {
      assert.strictEqual(calculateNumber(3.7, 1), 5);
    });
  });

    describe('2nd rounded', function () {
    it('return 5', function () {
      assert.strictEqual(calculateNumber(1, 5.2), 6);
    });
  });

  describe('Two floats', function () {
    it('return 5', function () {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });
  });
});
