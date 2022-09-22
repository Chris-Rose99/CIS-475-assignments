import sys

def strxor(a, b):
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

        zip("0010".decode("hex"), "0104".decode("hex"))

if __name__=='__main__':
    cipher1 = "790f3af3e425c6e6ce52ed0946039a0dba682ba30288cf33d1af8677cf9df4191f72b6567da54a4f81d90937d3ff547cef04e3d80c68481c247f12d3733b647a90c849c4e74dbd4ab9f4d5be7701dcb7adde002a0ebcb6886c".decode('hex')
    cipher2 = "7c0c6ea0fe3b83e7cf43ed00451f940dbb6826e85094cf33d1b3837bc9cffa194634ba4b6ea11844cf901e78c0e8156da00be6d9586c485f717802d37326647588dd1bf8c67d9c19f4".decode('hex')
    cipher3 = "790f3af9e43d83fbc541a80d46508642ac7b65f0159ed376c4aec46ad4cfe1030372a25077a4460096960578d5e51b6aec0db3c317791a5268770b963a3c2c71dfcb00f3cc388905a8bbcaab7410d8a9e4d1097317bba18062630f9543a7bdb7c887027ca60f".decode('hex')
    cipher4 = "7e066ea0ea2ed1e8c953ed034c509748b06e2df703ddc075c2bc8d7a9b80f34b113bb14d71b344".decode('hex')
    cipher5 = "64017fa0e827cdedc943a4034450904bf9682bfa509fc070dba8943ed29cb51e0839bb566eae4a55818d193486ec546de51ae7c20a681a59773607876e2d29648bd90db3".decode('hex')
    cipher6 = "67017feeab21d7a9c358a00959508b42f97937ea069cc26a90bc8a7a9b8ef6080927bb4d78a2034c868d097486fd1170f005f68d19614d517d6546977f25257a9b9c1df5cd388905a8f6ddbc2213d6b7adcb06360ea0a1813472139556a1bcb7c89d0239b94056a698ed3ab0158c16ed25f62e65dded7a3c342e6ad56a".decode('hex')
    cipher7 = "711a3ae1e53183efc145a00958508844b56565f71591cd33c9b291329b80fb071f72b4197faf054ccf95152cd5ad153fe606eb8d1f785b426036129b7f682c7191d406e8db7dcf0eb5f4cae0".decode('hex')
    cipher8 = "720c6ef4ee3a83ebc517a9095900965ebc6d65e51f8f8167dfb2c47fd597fc041321f55869b01845879c1e2bcfe21a6cac49e7c519631a42717f08967e68266ddfc806f2887b8004bcf2dcab6c0199b6e8dc1b210aa7bdc3".decode('hex')
    cipher9 = "69066fa0e829cde7cf43ed04451c9b0dbf6037e6079ccd7fc3fd8570dfcffc051220a04a70af04008b9c043dc5f91d70ee49e0d40b795f5d773607907927317a8bdd0bf1cd36cf33b5ee98ad631b99aae3d317730bbca889626705da47a3bdb7dd960476a04f56b39ff37ff8".decode('hex')
    cipher10 = "791d3ae9f868cefcc35fed0145029a0daa6c26f602988167dffd867b9b89f00a1437b1196da80b4ecf8d1f78c4e85473ef1ff6c956".decode('hex')
    xorcipher = strxor(cipher1,cipher2) # Once you know one you can figure them all out
    xorcrib1 = strxor(xorcipher,"If someone else can run arbitrary code on your computer, it is not YOUR computer anymore.") # put in message A to get message B or guess with repeated sequence of random words
    print "xorcrib1: ", xorcrib1
    xorcrib2 = strxor(xorcipher,"can can can can backn can can can can can can can can can can can can can can can can can can can can can can can can can ") # put in message B to get message A or guess with repeated sequence of random words
    print "xorcrib2: ", xorcrib2

    xorkey = strxor("It is much more secure to be feared than to be loved.", "791d3ae9f868cefcc35fed0145029a0daa6c26f602988167dffd867b9b89f00a1437b1196da80b4ecf8d1f78c4e85473ef1ff6c956".decode('hex'))
    print xorkey # This will return the key for the cipher and corresponding message above ^
    xormess = strxor(xorkey, "67017feeab21d7a9c358a00959508b42f97937ea069cc26a90bc8a7a9b8ef6080927bb4d78a2034c868d097486fd1170f005f68d19614d517d6546977f25257a9b9c1df5cd388905a8f6ddbc2213d6b7adcb06360ea0a1813472139556a1bcb7c89d0239b94056a698ed3ab0158c16ed25f62e65dded7a3c342e6ad56a".decode('hex'))
    print xormess # should return the plain text for the cipher above ^

    #message 1: If someone else can run arbitrary code on your computer, it is not YOUR computer anymore.
    #message 2: Let us not look back in anger or forward in fear but around in awareness.
    #message 3: If you reveal your secrets to the wind, you should not blame the wind for revealing them to the trees.
    #message 4: Not afraid of heights afraid of widths.
    #message 5: The condition of any backup is unknown until a restore is attempted.
    #message 6: When it comes to privacy and accountability, people always demand the former for themselves and the latter for everyone else.
    #message 7: As any farmer will tell you, only a fool lets a fox guard the henhouse door.
    #message 8: Better be despised for too anxious apprehensions, than ruined by too confident security.
    #message 9: You cannot hold firewalls and intrusion detection systems accountable. You can only hold people accountable.
    #message10: It is much more secure to be feared than to be loved.