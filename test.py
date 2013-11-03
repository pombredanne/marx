from marx.docker.wrapper import Docker

d = Docker()

for x in d.attach('5e54062461cf'):
    print x
