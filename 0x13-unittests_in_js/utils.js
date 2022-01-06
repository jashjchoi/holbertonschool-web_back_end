const Utils = {
  calculateNumber(type, x, y) {
    const xRound = Math.round(x);
    const yRound = Math.round(y);

    if (type === 'DIVIDE') {
        if (yRound === 0) {
        return 'Error';
        }
        return xRound / yRound;
    }

    if (type === 'SUBTRACT') {
        return xRound - yRound;
    }

    return xRound + yRound;
    },
};
module.exports = Utils;
