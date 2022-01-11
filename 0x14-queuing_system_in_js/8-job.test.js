import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';
const queue = kue.createQueue();
const jobData = [
  {
    phoneNumber: '001',
    message: 'This is the sample 1',
  },
  {
    phoneNumber: '900',
    message: 'This is the sample 2',
  },
];

describe('createPushNotificationsJobs', () => {
  before(function () {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

 // Fail cases
  it('display a error message if jobs is not an array; Invalid num value', () => {
    expect(() => {
      createPushNotificationsJobs(1, queue);
    }).to.throw('Jobs is not an array');
  });

  it('display a error message if jobs is not an array; NaN', () => {
    expect(() => {
      createPushNotificationsJobs({}, queue);
    }).to.throw('Jobs is not an array');
  });

  it('display a error message if jobs is not an array; Invalid string value', () => {
    expect(() => {
      createPushNotificationsJobs('dummy', queue);
    }).to.throw('Jobs is not an array');
  });

    // Success cases
  it('create two new jobs to the queue', () => {
    createPushNotificationsJobs(jobData, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobData[0]);
    expect(queue.testMode.jobs[1].data).to.eql(jobData[1]);
  });
});
