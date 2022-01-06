const sinon = require('sinon');
const { expect }  = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const utils = require('./utils')


describe('Spies', function () {
  it('Spies output:', () => {
    const spyFunction = sinon.spy(utils, 'calculateNumber');
    const spyConsole = sinon.spy(console, 'log');

    expect(spyFunction.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(spyConsole.calledOnceWithExactly('The total is: 120')).to.be.true;

    spyFunction.restore();
    spyConsole.restore();
  });
});
