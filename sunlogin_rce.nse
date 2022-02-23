---
-- @usage
-- nmap --script sunlogin_rce <target>
--
-- @output
-- PORT    STATE SERVICE
-- 49194/tcp open  unknown 
-- |_sunlogin_rce: Likely to be Sunlogin_RCE port!
--


local http = require "http"

local path = "/"
local result

portrule = function(host, port)
  result = http.get(host, port, path)
  return result and result.status
end

action = function(host, port)
  if result.body == "{\"success\":false,\"msg\":\"Verification failure\"}" then
    return "Likely to be Sunlogin_RCE port!"
  end
end
