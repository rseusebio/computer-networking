const dgram = require('node:dgram');
const { Buffer } = require('node:buffer');

const client = dgram.createSocket('udp4');
const port = 12000;
const address = '127.0.0.1';


const async_send = async (message) => {
    return new Promise((resolve, reject) => {
        client.send(Buffer.from(message), port, address, (err) => {
            if (err) {
                return reject(err);
            }
            resolve('sent');
        });

    })
}

const main = async () => {
    const N = 100;
    const promises = [];
    for (let i = 0; i < N; i++) {
        promises.push(
            async_send((i + 1).toString())
        );
    }
    await Promise.all(promises).catch(err => console.error(err));
}

main().then(() => console.log('done'));