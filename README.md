# Bitcoin Edu

API: https://bitcoin.org/en/developer-reference#block-headers

Local server: https://github.com/bitcoinedu-io/bitcoinedu/releases/tag/v0.16.3

Local server config:
<pre>
server=1
rpcuser=userbob
rpcpassword=secret
txindex=1
reindex=1 # only first time starting
</pre>
## Example output
<pre>
====================================================================================================
Antal block:                   30579
Lagringsstorlek:               10719073
Högsta validerade best-block:  00000000978bddf13bb12075b6cf2fa895a8911b773c0a6665f2d049cd6fb5b8
Mempool (size):                0 st transaktioner
Anslutningar:                  3 noder
====================================================================================================

Meny
 1. Visa block (ange nr)
 2. Visa block (ange hash)
 3. Visa transaktion
 4. Lista outputs för adress

 5. Visa startinfo
 0. Avsluta

Välj funktion: 1
Ange block-nummer: 3125
----------------------------------------------------------------------------------------------------
Block hash:             000000001cf04f9f33bd764a3040a06e6688094bac6ec2f173c74c576ef47b4f
Föregående hash:        000000006adf2dc33c31af5b3ae4c5f0f85755ea88f12c2854504c52fb7b879f
Merkle root:            25f8932e1b303f1d3be694c95395f240410f04e9884253732b4f411e0b3ae363
Höjd:                   3125
Tid:                    2018-02-27 17:46:25
Svårighet:              1.522476478104309
Antal transaktioner:    5
Transaktioner:
  0 : a29ad6390646bc495fb8d6b6571f1b75455b3914d6e3867631f7eee95097ed50
  1 : 07979bb627f9221b43023225a9096b1b46b069b4a9e4d8afef7292db90d9e05e
  2 : 2672fd5f74903ce000c880915a40709ceed0d8c2bd91e2a2ec9711d799eec01d
  3 : 56199e6a587842d7deb8dbe58bbdbcf13928eefb82dbf6d4c175663f6afd8588
  4 : 24a142b84a3d31e0f5df77f660096f85a1ba42456ee3765d818cb999dbeb6235
----------------------------------------------------------------------------------------------------

Meny
 1. Visa block (ange nr)
 2. Visa block (ange hash)
 3. Visa transaktion
 4. Lista outputs för adress

 5. Visa startinfo
 0. Avsluta

Välj funktion: 2
Ange transaktionshash: 000000006adf2dc33c31af5b3ae4c5f0f85755ea88f12c2854504c52fb7b879f
----------------------------------------------------------------------------------------------------
Block hash:             000000006adf2dc33c31af5b3ae4c5f0f85755ea88f12c2854504c52fb7b879f
Föregående hash:        000000006e36b0407ad27115e5706d210bf913cf5745ae51ad36d0471ff82e1c
Merkle root:            aa971d1e6c85a576da64bc885a2c5c4f27901eab39a2e3c3a48e744290c5b87a
Höjd:                   3124
Tid:                    2018-02-27 17:11:14
Svårighet:              1.522476478104309
Antal transaktioner:    1
Transaktioner:
  0 : aa971d1e6c85a576da64bc885a2c5c4f27901eab39a2e3c3a48e744290c5b87a
----------------------------------------------------------------------------------------------------

Meny
 1. Visa block (ange nr)
 2. Visa block (ange hash)
 3. Visa transaktion
 4. Lista outputs för adress

 5. Visa startinfo
 0. Avsluta

Välj funktion: 3
Ange transaktionshash: aa971d1e6c85a576da64bc885a2c5c4f27901eab39a2e3c3a48e744290c5b87a
----------------------------------------------------------------------------------------------------
Txid (hash):             aa971d1e6c85a576da64bc885a2c5c4f27901eab39a2e3c3a48e744290c5b87a
Tillhör block:           000000006adf2dc33c31af5b3ae4c5f0f85755ea88f12c2854504c52fb7b879f
Inputs:                  1
Outputs:                  2
1 : 50.0 BTE till 1eduGsrvBJcfyTMij2rYXk9viiVV78PNq
2 : 0.0 BTE till adress saknas
----------------------------------------------------------------------------------------------------

Meny
 1. Visa block (ange nr)
 2. Visa block (ange hash)
 3. Visa transaktion
 4. Lista outputs för adress

 5. Visa startinfo
 0. Avsluta

Välj funktion: 4
Ange adress: 1eduGsrvBJcfyTMij2rYXk9viiVV78PNq
Hittade inget bra RPC anrop att använda, så handjagar detta på klientsidan, 
vilket är idiotiskt då det blir en jävla massa anrop.
CTRL + C, för att avbryta.
--------
Söker på index: 1/30579
Söker på index: 2/30579
Söker på index: 3/30579
</pre>
