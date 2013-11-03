from marx.docker.wrapper import Docker

d = Docker()

for x in d.rm("06c4d470bea5"):
    print x
