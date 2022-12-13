# Developing PCBDL

This command will setup the development enviroment so it will be easy to make changes to PCBDL:
```bash
sudo pip3 install -r requirements.txt
```

You probably also want to [install netlistsvg](https://google.github.io/pcbdl/doc/_build/html/netlistsvg.html#installation).

## Tests

To test pcbdl framework functionality (not the schematics themselves), one can run:
```bash
make test
```

If everything passes the code coverage can be seen with:
```bash
make show-coverage
```

## Contributor License Agreement

Contributions to this project must be accompanied by a Contributor License
Agreement. You (or your employer) retain the copyright to your contribution;
this simply gives us permission to use and redistribute your contributions as
part of the project. Head over to <https://cla.developers.google.com/> to see
your current agreements on file or to sign a new one.

You generally only need to submit a CLA once, so if you've already submitted one
(even if it was for a different project), you probably don't need to do it
again.
