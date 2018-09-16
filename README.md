# Simple todo

Simple todo task list is only API not include user interface. Create with django-rest-framework.

## Installation
- Build docker image

```$ docker-compose build```

- Start  project with docker-compose

```$ docker-compose up```

- First run use this command for migrate database

 ```$ docker-compose exec django python manage.py migrate```
 
- Run this command for test

```$ docker-compose exec django python manage.py test```

Check status [http://localhost:8000]() 

Route view of API: [http://localhost:8000/api]()

API Document: [http://localhost:8000/docs]()

## License
 
The MIT License (MIT)

Copyright (c) 2018 [Supayut Raksuk](github.com/nookskill)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
