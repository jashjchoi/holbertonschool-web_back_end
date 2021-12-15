export default function guardrail(mathFunction) {
  const queue = [];
  let func;
  try {
    func = mathFunction();
  } catch (err) {
    func = `${err.name}: ${err.message}`;
  }
  queue.push(func);
  queue.push('Guardrail was processed');
  return queue;
}
