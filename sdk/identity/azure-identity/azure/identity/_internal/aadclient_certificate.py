# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import base64
from typing import Optional
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.backends import default_backend


class AadClientCertificate:
    """Wraps 'cryptography' to provide the crypto operations AadClient requires for certificate authentication.

    :param bytes pem_bytes: bytes of a a PEM-encoded certificate including the (RSA) private key
    :param bytes password: (optional) the certificate's password
    """
    def __init__(
            self,
            pem_bytes: bytes,
            password: Optional[bytes] = None
    ) -> None:
        private_key = serialization.load_pem_private_key(pem_bytes, password=password, backend=default_backend())
        if not isinstance(private_key, RSAPrivateKey):
            raise ValueError("The certificate must have an RSA private key because RS256 is used for signing")
        self._private_key = private_key

        cert = x509.load_pem_x509_certificate(pem_bytes, default_backend())
        fingerprint = cert.fingerprint(hashes.SHA1())  # nosec
        self._thumbprint = base64.urlsafe_b64encode(fingerprint).decode("utf-8")

    @property
    def thumbprint(self) -> str:
        """The certificate's SHA1 thumbprint as a base64url-encoded string"""
        return self._thumbprint

    def sign(self, plaintext: bytes) -> bytes:
        """Sign bytes using RS256"""
        return self._private_key.sign(plaintext, padding.PKCS1v15(), hashes.SHA256())
