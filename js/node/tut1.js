const path_tut = () => {
  const path = require('path')
  const file = path.parse(__filename)
  console.log(file)
}

const os_tut = () => {
  const os = require('os')
  console.log(`Free Memory: ${freemem} , Total Memory: ${totalmem}`)
}

const fs_tut = () => {
  const fs = require('fs')
  console.log(fs.readdir('./', (err, files) => {
    if (err) {
      console.log('Error:', err)
    } else {
      console.log('Result:', files)
    }
  }))
}

const events_tut = () => {
  const EventEmitter = require('events')
  class Logger extends EventEmitter {
    log(message) {
      console.log(message)
      this.emit('messageLogged', { id: 1, name: "First Log" })
    }
  }
  const logger = new Logger()
  logger.on('messageLogged', (args) => {
    console.log(`Message id: ${args.id}, Message Name: ${args.name}`)
  })
  logger.log('Log 101')
}

const http_tut = () => {
  const http = require('http')
  const server = http.createServer((req, res) => {
    if (req.url === '/') {
      res.write('Hello World!')
      res.end()
    } else if (req.url === '/api/courses') {
      res.write(JSON.stringify(
        [
          {
            course_code: 'CSE101',
            name: 'Introduction to Programming'
          },
          {
            course_code: 'MTH101',
            name: 'Linear Algebra'
          }
        ]
      ))
      res.end()
    }
  })

  server.listen(3000)
  console.log('Listening at port 3000')
}

http_tut()