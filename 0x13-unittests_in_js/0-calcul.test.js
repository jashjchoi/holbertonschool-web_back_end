const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  describe('Integers', function () {
    it('return 4', function () {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });
  });

  describe('One float', function () {
    it('return 5', function () {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
  });

    describe('Two floats', function () {
    it('return 5', function () {
      assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
  });

  describe('Two floats', function () {
    it('return 5', function () {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });
  });
});
