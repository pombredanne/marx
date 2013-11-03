from marx.docker.wrapper import Docker

d = Docker()
print list(d.images())
