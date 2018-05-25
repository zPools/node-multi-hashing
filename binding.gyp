{
    "targets": [
        {
            "target_name": "multihashing",
            "sources": [
                "multihashing.cc",
                "scryptjane.c",
                "scryptn.c",
                "keccak.c",
                "skein.c",
                "x11.c",
		"bitcore.c",
		"gost.c",
                "quark.c",
                "bcrypt.c",
                "groestl.c",
		"allium.c",
                "blake.c",
                "fugue.c",
                "qubit.c",
                "hefty1.c",
                "shavite3.c",
                "x13.c",
                "nist5.c",
                "sha1.c",
                "whirlpoolx.c",
                "x15.c",
		"whirlpoolx.c",
		"zr5.c",
		"tribus.c",
		"sonoa.c",
		"x14.c",
		"skunk.c",
		"jha.c",
                "fresh.c",
		"hsr.c",
		"neoscrypt.c",
		"blake2s.c",
		"Lyra2RE/Lyra2.c",
		"Lyra2RE/Lyra2RE.c",
		"Lyra2RE/Lyra2Z.c",
		"Lyra2RE/Lyra2H.c",
		"Lyra2RE/Sponge.c",
		"Lyra2RE/vtc_blake.c",
		"Lyra2RE/vtc_bmw.c",
		"Lyra2RE/vtc_cubehash.c",
		"Lyra2RE/vtc_groestl.c",
		"Lyra2RE/vtc_keccak.c",
		"Lyra2RE/vtc_skein.c",
		"sha3/sph_blake2s.c",
                "sha3/sph_hefty1.c",
                "sha3/sph_fugue.c",
                "sha3/aes_helper.c",
                "sha3/sph_echo.c",
                "sha3/sph_jh.c",
                "sha3/sph_luffa.c",
                "sha3/sph_shavite.c",
                "sha3/sph_simd.c",
                "sha3/sph_whirlpool.c",
                "sha3/sph_shabal.c",
                "sha3/hamsi.c",
		"sha3/sph_gost.c",
		"sha3/sph_sm3.c",
                "crypto/oaes_lib.c",
                "crypto/c_keccak.c",
                "crypto/c_groestl.c",
                "crypto/c_blake256.c",
                "crypto/c_jh.c",
                "crypto/c_skein.c",
                "crypto/hash.c",
                "crypto/aesb.c",
                "crypto/wild_keccak.cpp",
            ],
            "include_dirs": [
                "crypto",
            ],
            "cflags_cc": [
                "-std=c++0x"
            ],
        }
    ]
}
