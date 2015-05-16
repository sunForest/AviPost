# pip wrapper for install and uninstall, automatically add or remove dependencies

# exit on error
set -e

# help screen
function help() {
cat << EOF
Usage: pip.sh <command> <target> [--prod|--dev|--ci]

Command:
    install
    uninstall
EOF
}

if [[ $1 == '--help' ]]; then
    help
    exit 0
fi

cmd="$1"

# shift arguments to parse switches
shift

while [[ $# > 0 ]]; do
    key="$1"
    case $key in
        --prod )
            env=prod
            shift
            ;;

        --dev )
            env=dev
            shift
            ;;

        --ci )
            env=ci
            shift
            ;;

        *)
            # what to install
            target=$key
            shift
            ;;
    esac
done

function delete_target() {
    # for compability between OS X and Linux we use temp files
    sed "/^$target==/d" > /tmp/$env.txt 
    cp /tmp/$env.txt requirements/$env.txt
}

if [[ $cmd == "install" ]]; then
    pip $cmd $target
    # delete first if exists
    delete_target
    # add
    pip freeze | grep $target >> requirements/$env.txt
elif [[ $cmd == "uninstall" ]]; then
    pip $cmd $target
    delete_target
else
    echo No command $1!!
    exit 1
fi
