# setup macro
ssh_port = 22222

# simple check

net.tcp.service[ssh,,{$SSH_PORT}] -> Check SSH port $3

-> return 1: open, return 0: off

