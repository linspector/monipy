"""
This file is part of monipy (https://hanez.org/monipy/)
Copyright (c) 2022 Johannes Findeisen <you@hanez.org>

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
"""

import atexit
import os
import signal
import sys
import time

from logging import getLogger

logger = getLogger('monipy')


class Daemon:
    # subclass the daemon class and override the run() method.

    def __init__(self, pid_file):
        self.__pid_file = pid_file

    def daemonize(self):
        # daemonize the class using the UNIX double fork mechanism.

        # do first fork.
        try:
            pid = os.fork()
            if pid > 0:
                # exit first parent.
                sys.exit(0)
        except OSError as err:
            logger.error(str('fork #1 failed: {0}'.format(err)))
            sys.exit(1)

        # decouple from parent environment.
        os.chdir('/')
        os.setsid()
        os.umask(0)

        # do second fork.
        try:
            pid = os.fork()
            if pid > 0:
                # Exit from second parent.
                sys.exit(0)
        except OSError as err:
            logger.error(str('fork #2 failed: {0}'.format(err)))
            sys.exit(1)

        # redirect standard file descriptors.
        sys.stdout.flush()
        sys.stderr.flush()
        si = open(os.devnull, 'r')
        so = open(os.devnull, 'a+')
        se = open(os.devnull, 'a+')

        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # write pid file.
        atexit.register(self.delete_pid)

        pid = str(os.getpid())
        with open(self.__pid_file, 'w+') as f:
            f.write(pid + '\n')

    def delete_pid(self):
        os.remove(self.__pid_file)

    def start(self):
        # start the daemon. check for a pidfile to see if the daemon already runs before.

        try:
            with open(self.__pid_file, 'r') as pf:
                pid = int(pf.read().strip())
        except IOError:
            pid = None

        if pid:
            message = 'pid_file {0} already exist. daemon already running?'
            logger.error(str(message.format(self.__pid_file)))
            sys.exit(1)

        # start the daemon.
        self.daemonize()
        self.run()

    def stop(self):
        # stop the daemon.

        # get the pid from the pid file.
        try:
            with open(self.__pid_file, 'r') as pf:
                pid = int(pf.read().strip())
        except IOError:
            pid = None

        if not pid:
            message = 'pid_file {0} does not exist. daemon not running?'
            logger.error(str(message.format(self.__pid_file)))
            return  # not an error in a restart

        # try killing the daemon process.
        try:
            while 1:
                os.kill(pid, signal.SIGTERM)
                time.sleep(0.1)
        except OSError as err:
            e = str(err.args)
            if e.find('no such process') > 0:
                if os.path.exists(self.__pid_file):
                    os.remove(self.__pid_file)
            else:
                logger.error(str(err.args))
                sys.exit(1)

    def restart(self):
        # restart the daemon.

        self.stop()
        self.start()

    def run(self):
        """
        you should override this method when you subclass daemon. it will be called after the
        process has been daemonized by start() or restart().
        """
