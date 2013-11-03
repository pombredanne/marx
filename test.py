from marx.docker.wrapper import Docker

d = Docker()
for image in d.images():
    print image
