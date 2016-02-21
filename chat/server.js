var express = require('express'),
    app = express(),
    server = require('http').createServer(app),
    io = require('socket.io').listen(server);

var PythonShell = require('python-shell');

var users = {};

server.listen(3000);

app.use(express.static('.'));

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

io.sockets.on('connection', function(socket){
  var pyshell = new PythonShell('proto.py', {pythonPath : 'python3', mode : 'text'});

  pyshell.on('message', function(message) {
    console.log(message);
    io.sockets.emit('new message', {msg: message, nick: socket.nickname});
  });

  pyshell.on('error', function(err) {
    console.log(err);
  });

  socket.on('new user', function(data, callback){
    if (data ==='' || data in users){
      callback(false);
    } else {
      callback(true);
      socket.nickname = data;
      users[socket.nickname] = socket;
      updateNicknames();
    }
  });

  function updateNicknames() {
    io.sockets.emit('usernames', Object.keys(users));
  }

  socket.on('send-message', function(data){
    var msg = data.trim();
    pyshell.send(msg);
    //io.sockets.emit('new message', {msg: data, nick: socket.nickname});
  });

  socket.on('disconnect', function(data){
    if(!socket.nickname) return;
    delete users[socket.nickname];
    updateNicknames();
  });
});
