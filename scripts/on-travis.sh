#!/bin/bash

openssl aes-256-cbc -K $encrypted_f182de71524d_key -iv $encrypted_f182de71524d_iv -in .prod.env.enc -out .prod.env -d

sudo apt update
sudo apt install sshpass

zip dist.zip ./*

sshpass -p "$SSH_PASS" scp dist.zip @SSH_HOST:~/isteam
sshpass -p "$SSH_PASS" ssh -o StrictHostKeyChecking=no $SSH_HOST < scripts/on-isteam.sh