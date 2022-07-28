package org.github.luolong47;

import cn.hutool.core.io.FileUtil;
import cn.hutool.crypto.BCUtil;
import cn.hutool.crypto.SecureUtil;
import cn.hutool.crypto.asymmetric.KeyType;
import cn.hutool.crypto.asymmetric.RSA;

import java.security.PublicKey;

public class Main {
    public static void main(String[] args) {
        PublicKey publicKey = BCUtil.readPemPublicKey(FileUtil.getInputStream("E:\\Downloads\\file_3\\pubkey.pem"));
        System.out.println(publicKey);
//        String priKey = FileUtil.readUtf8String("E:\\Downloads\\file_3\\privatekey.pem");
//        System.out.println(priKey);
//        PrivateKey privateKey = BCUtil.readPemPrivateKey(FileUtil.getInputStream("E:\\Downloads\\file_3\\privatekey.pem"));
//        System.out.println(privateKey);
        RSA rsa = SecureUtil.rsa(null, publicKey.getEncoded());
        byte[] decrypt = rsa.decrypt(FileUtil.readBytes("E:\\Downloads\\file_3\\pubkey.pem"), KeyType.PublicKey);

        System.out.println(decrypt);
    }
}
