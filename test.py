from marx.docker.wrapper import Docker

d = Docker()
for image in d.ps(a=True):
    print image
