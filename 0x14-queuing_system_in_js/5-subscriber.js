import redis from 'redis';

const subs = redis.createClient();
const channel = 'holberton school channel';

subs.on('ready', () => console.log('Redis client connected to the server'));

subs.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

subs.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subs.unsubscribe();
    subs.quit();
  }
});

subs.subscribe(channel);
