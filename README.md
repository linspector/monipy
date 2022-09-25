# monipy - A infrastructure monitoring toolchain

This is implemented in an old school way for easy understanding without cloud
and such stuff... Hope it will become useful someday for somebody and not only for
me.

## About

**monipy** contains some tools and a daemon to monitor your infrastructure. It
collects data for statistics and sends alerts in case of errors.

This project is at a very early stage of development it is not able for usage.
I design the software actually and try to convert my ideas to software. Code
nearly does not exist.

## Development

### To do

**Everything!** :) Just outlining the idea and creating code and structure skeletons
at the moment!

### Ideas

- MAYBE rename this project to linspector and see it as an update. This is a nice idea 
because [Linspector](https://hanez.org/linspector/) has it's GitHub organisation, 
domain etc. And all I do here is 
a better Linspector. Even all nice and useful features and ideas from Linspector but 
also uplink should be reimplemented here.

- Think about adding [APScheduler](https://pypi.org/project/APScheduler/) for 
scheduling execution of the monitors instead of a self constructed thread
structure... was very nice to get the job done in Linspector.

### Manifest

- All of this project **must be MIT licensed**. When using 3rd party libraries make
sure the license is compatible but MIT should always be preferred if an
alternative is available.
- The core of monipy/monipyd should not use 3rd party libraries. only plugins,
notifications and types may use other libraries. But coping code into the
source tree is ok when respecting the license. Not using 3rd party libraries
should always be preferred though.
- Inline comment should be all lowercase. Descriptions and documentation comments
must be natural language.

### Version numbering

According to: [https://wiki.unixpeople.org/linux_kernel_version_numbering](https://wiki.unixpeople.org/linux_kernel_version_numbering)

**MAJOR**.**FEATURE**.**MINOR**.**FIXES**

- **MAJOR** changes _can_ change the API. The lesser, the better.
- **FEATURE** changes can, but _should_ not break the API. New features are placed
  here. It _expects_ a complete documentation.
- **MINOR** changes are "just-in-time" changes or small enhancements which _should_
  not affect the documentation and _must_ not break the API.
- **FIXES** _must_ never affect anything else then stability or security.

## License

### MIT License

Copyright (c) 2022 Johannes Findeisen &lt;you@hanez.org&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice (including the next
paragraph) shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
