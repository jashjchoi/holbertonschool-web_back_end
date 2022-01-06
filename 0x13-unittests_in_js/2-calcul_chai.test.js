const {expect} = require('chai');
const calculateNumber = require('./2-calcul_chai.js');


describe('SUM', () => {
  it('return rounded number', () => {
    expect(calculateNumber('SUM', 4, 3)).to.equal(7);
    expect(calculateNumber('SUM', 1.8, 0)).to.equal(2);
    expect(calculateNumber('SUM', 5.1, 3.1)).to.equal(8);
  });
});

describe('SUBTRACT', () => {
  it('return rounded number', () => {
    expect(calculateNumber('SUBTRACT', 4, 3)).to.equal(1);
    expect(calculateNumber('SUBTRACT', 1.8, 0)).to.equal(2);
    expect(calculateNumber('SUBTRACT', 5.1, 3.1)).to.equal(2);
  });
});

describe('DIVIDE', () => {
  it('return rounded positive divide', () => {
    expect(calculateNumber('DIVIDE', 6, 2)).to.equal(3);
    expect(calculateNumber('DIVIDE', 6.1, 1.8)).to.equal(3);
    expect(calculateNumber('DIVIDE', 4.9, 5)).to.equal(1);
  });
  it('return Error', () => {
    expect(calculateNumber('DIVIDE', 1, 0)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 3, 0)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 2.5, 0)).to.equal('Error');
  });
});
