
This project is experimental.

Using [pyramid_redis] as an example.

[pyramid_zmq][] integrating [zmq][] with a [Pyramid][] web application.

### Usage

    config.include('pyramid_zmq')

### Configuration

Requires one of the the following [INI setting / environment variable][]:

* `zmq.url` Default url required
* `zmq.pushpull.url` Used for push/pull if given
* `zmq.pubsub.url` Used for pub/sub if given
