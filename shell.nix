{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    firefox
    geckodriver
    (python311.withPackages(ps: with ps; [ selenium ]))  # paramiko ]))
  ];

  shellHook = ''
    ssh_tunnel_port=5055
    # proxy over ssh (fork to bg, compress, quiet, no remote command)
    ssh -D $ssh_tunnel_port -fCqN x07

    # export http_proxy=socks5h://0:$ssh_tunnel_port

    echo "proxy running over ssh tunnel ..."
    echo "http_proxy: $http_proxy"

    echo -e "\nDebug info:"
    ss -tlpn | grep $ssh_tunnel_port
  '';
}
