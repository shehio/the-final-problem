## Following these steps: https://docs.bitnami.com/tutorials/deploy-redis-cluster-tmc-helm-chart/#step-5-deploy-the-bitnami-redis-cluster-helm-chart-by-enabling-external-access

helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

helm install my-redis bitnami/redis-cluster --set cluster.externalAccess.enabled=true

export REDIS_PASSWORD=$(kubectl get secret --namespace "default" my-redis2-redis-cluster -o jsonpath="{.data.redis-password}" | base64 -d)

helm upgrade my-redis --set password=$REDIS_PASSWORD --set "cluster.externalAccess.enabled=true,cluster.externalAccess.service.type=LoadBalancer,cluster.externalAccess.service.loadBalancerIP[0]=load-balancerip-0,cluster.externalAccess.service.loadBalancerIP[1]=load-balancerip-1,cluster.externalAccess.service.loadBalancerIP[2]=load-balancerip-2,cluster.externalAccess.service.loadBalancerIP[3]=load-balancerip-3,cluster.externalAccess.service.loadBalancerIP[4]=load-balancerip-4,cluster.externalAccess.service.loadBalancerIP[5]=load-balancerip-5" oci://registry-1.docker.io/bitnamicharts/
