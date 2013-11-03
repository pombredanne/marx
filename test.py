from marx.docker.wrapper import Docker

d = Docker()

for x in d.events():
    print x
