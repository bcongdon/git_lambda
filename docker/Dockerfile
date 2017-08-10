FROM amazonlinux
RUN yum install git cmake -y
RUN yum groupinstall 'Development Tools' -y

RUN yum install dh-autoreconf curl-devel expat-devel \
    gettext-devel openssl-devel perl-devel zlib-devel -y

RUN curl https://www.kernel.org/pub/software/scm/git/git-2.14.0.tar.gz > git-source.tar.gz && \
    tar -zxf git-source.tar.gz && \
    cd git-2.14.0 && \
    make configure && \
    mkdir /git && \
    ./configure --prefix=/git CFLAGS="${CFLAGS} -static-libgcc" && \
    make all && \
    make install && \
    cd /git/share && \
    find . -maxdepth 1 ! -name 'git-core' ! -path . -delete && \
    cd / && \
    tar -zcvf git-2.14.0.tar.gz git
