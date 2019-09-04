import argparse
import jwt

class JwtTokenValidator:
    def execute(self, args):
        self.parser = self.initParser()
        parsedArgs = self.parser.parse_args(args)

        secret = ''
        with open(parsedArgs.publicKey, 'r') as f:
            secret = f.read()

        alg = 'RS256'
        if parsedArgs.algorithm is not None:
            alg = parsedArgs.algorithm.upper()

        decoded = jwt.decode(parsedArgs.token, secret, algorithms=alg)
        print(decoded)

    def initParser(self):
        parser = argparse.ArgumentParser(prog='forge verify-jwt')
        parser.add_argument('-t', '--token', action='store', dest='token', required=True,
                            help='valid jwt token that is generated using a private key matching the public key argument')
        parser.add_argument('-p', '--publickey', action='store', dest='publicKey', required=True,
                            help='the public key to decode token')
        parser.add_argument('-alg', '--algorithm', action='store', dest='algorithm',
                            help='the algorithm used to sign the token, the default is RS256')
        return parser