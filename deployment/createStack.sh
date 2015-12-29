SecretKey=$(openssl rand -base64 30)
DBPassword="dfjslkjls"
aws cloudformation create-stack --stack-name avipost2 --template-body \
file://./avipost.api.cftemplate.json \
--parameters ParameterKey=SecretKey,ParameterValue=$SecretKey \
ParameterKey=DBPassword,ParameterValue=$DBPassword --capabilities CAPABILITY_IAM
