PGDMP     
                    x            how_to_build    12.2    12.2 =    [           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            \           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ]           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ^           1262    74460    how_to_build    DATABASE     �   CREATE DATABASE how_to_build WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Russian_Russia.1251' LC_CTYPE = 'Russian_Russia.1251';
    DROP DATABASE how_to_build;
                postgres    false            �            1259    74490 	   districts    TABLE     `   CREATE TABLE public.districts (
    id bigint NOT NULL,
    value character varying NOT NULL
);
    DROP TABLE public.districts;
       public         heap    postgres    false            �            1259    74488    districts_id_seq    SEQUENCE     y   CREATE SEQUENCE public.districts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.districts_id_seq;
       public          postgres    false    205            _           0    0    districts_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.districts_id_seq OWNED BY public.districts.id;
          public          postgres    false    204            �            1259    74501    houses    TABLE     �   CREATE TABLE public.houses (
    id bigint NOT NULL,
    laying_depth real,
    number character varying NOT NULL,
    street_id bigint NOT NULL,
    district_id bigint NOT NULL
);
    DROP TABLE public.houses;
       public         heap    postgres    false            �            1259    74499    houses_id_seq    SEQUENCE     v   CREATE SEQUENCE public.houses_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.houses_id_seq;
       public          postgres    false    207            `           0    0    houses_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.houses_id_seq OWNED BY public.houses.id;
          public          postgres    false    206            �            1259    74575    roles_id_seq    SEQUENCE     u   CREATE SEQUENCE public.roles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.roles_id_seq;
       public          postgres    false            �            1259    74543    roles    TABLE     �   CREATE TABLE public.roles (
    id bigint DEFAULT nextval('public.roles_id_seq'::regclass) NOT NULL,
    value character varying NOT NULL
);
    DROP TABLE public.roles;
       public         heap    postgres    false    215            �            1259    74471    streets    TABLE     Y   CREATE TABLE public.streets (
    id bigint NOT NULL,
    value character(1) NOT NULL
);
    DROP TABLE public.streets;
       public         heap    postgres    false            �            1259    74469    streets_id_seq    SEQUENCE     w   CREATE SEQUENCE public.streets_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.streets_id_seq;
       public          postgres    false    203            a           0    0    streets_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.streets_id_seq OWNED BY public.streets.id;
          public          postgres    false    202            �            1259    74578    tube_samples_id_seq    SEQUENCE     |   CREATE SEQUENCE public.tube_samples_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.tube_samples_id_seq;
       public          postgres    false            �            1259    74533    tube_samples    TABLE     �   CREATE TABLE public.tube_samples (
    " id" bigint DEFAULT nextval('public.tube_samples_id_seq'::regclass) NOT NULL,
    depth real,
    value real,
    tube_id bigint,
    date timestamp without time zone NOT NULL
);
     DROP TABLE public.tube_samples;
       public         heap    postgres    false    216            �            1259    74522    tubes    TABLE     [   CREATE TABLE public.tubes (
    id bigint NOT NULL,
    depth real,
    house_id bigint
);
    DROP TABLE public.tubes;
       public         heap    postgres    false            �            1259    74520    tubes_id_seq    SEQUENCE     u   CREATE SEQUENCE public.tubes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.tubes_id_seq;
       public          postgres    false    209            b           0    0    tubes_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.tubes_id_seq OWNED BY public.tubes.id;
          public          postgres    false    208            �            1259    74559 
   user_roles    TABLE     ]   CREATE TABLE public.user_roles (
    user_id bigint NOT NULL,
    role_id bigint NOT NULL
);
    DROP TABLE public.user_roles;
       public         heap    postgres    false            �            1259    74550    users    TABLE     �   CREATE TABLE public.users (
    id bigint NOT NULL,
    login character varying NOT NULL,
    password character varying,
    token_id bigint
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1259    74548    users_id_seq    SEQUENCE     u   CREATE SEQUENCE public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.users_id_seq;
       public          postgres    false    213            c           0    0    users_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;
          public          postgres    false    212            �            1259    74581    users_token_id_seq    SEQUENCE     {   CREATE SEQUENCE public.users_token_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.users_token_id_seq;
       public          postgres    false            �
           2604    74493    districts id    DEFAULT     l   ALTER TABLE ONLY public.districts ALTER COLUMN id SET DEFAULT nextval('public.districts_id_seq'::regclass);
 ;   ALTER TABLE public.districts ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    204    205    205            �
           2604    74504 	   houses id    DEFAULT     f   ALTER TABLE ONLY public.houses ALTER COLUMN id SET DEFAULT nextval('public.houses_id_seq'::regclass);
 8   ALTER TABLE public.houses ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    206    207    207            �
           2604    74474 
   streets id    DEFAULT     h   ALTER TABLE ONLY public.streets ALTER COLUMN id SET DEFAULT nextval('public.streets_id_seq'::regclass);
 9   ALTER TABLE public.streets ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203            �
           2604    74525    tubes id    DEFAULT     d   ALTER TABLE ONLY public.tubes ALTER COLUMN id SET DEFAULT nextval('public.tubes_id_seq'::regclass);
 7   ALTER TABLE public.tubes ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    208    209    209            �
           2604    74553    users id    DEFAULT     d   ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);
 7   ALTER TABLE public.users ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    213    212    213            �
           2604    74585    users token_id    DEFAULT     j   ALTER TABLE ONLY public.users ALTER COLUMN token_id SET DEFAULT nextval('public.users_id_seq'::regclass);
 =   ALTER TABLE public.users ALTER COLUMN token_id DROP DEFAULT;
       public          postgres    false    212    213    213            L          0    74490 	   districts 
   TABLE DATA           .   COPY public.districts (id, value) FROM stdin;
    public          postgres    false    205   �A       N          0    74501    houses 
   TABLE DATA           R   COPY public.houses (id, laying_depth, number, street_id, district_id) FROM stdin;
    public          postgres    false    207   �A       R          0    74543    roles 
   TABLE DATA           *   COPY public.roles (id, value) FROM stdin;
    public          postgres    false    211   �A       J          0    74471    streets 
   TABLE DATA           ,   COPY public.streets (id, value) FROM stdin;
    public          postgres    false    203   3B       Q          0    74533    tube_samples 
   TABLE DATA           J   COPY public.tube_samples (" id", depth, value, tube_id, date) FROM stdin;
    public          postgres    false    210   PB       P          0    74522    tubes 
   TABLE DATA           4   COPY public.tubes (id, depth, house_id) FROM stdin;
    public          postgres    false    209   mB       U          0    74559 
   user_roles 
   TABLE DATA           6   COPY public.user_roles (user_id, role_id) FROM stdin;
    public          postgres    false    214   �B       T          0    74550    users 
   TABLE DATA           >   COPY public.users (id, login, password, token_id) FROM stdin;
    public          postgres    false    213   �B       d           0    0    districts_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.districts_id_seq', 1, false);
          public          postgres    false    204            e           0    0    houses_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.houses_id_seq', 1, false);
          public          postgres    false    206            f           0    0    roles_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.roles_id_seq', 6, true);
          public          postgres    false    215            g           0    0    streets_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.streets_id_seq', 1, false);
          public          postgres    false    202            h           0    0    tube_samples_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.tube_samples_id_seq', 1, false);
          public          postgres    false    216            i           0    0    tubes_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.tubes_id_seq', 1, false);
          public          postgres    false    208            j           0    0    users_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.users_id_seq', 1, true);
          public          postgres    false    212            k           0    0    users_token_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.users_token_id_seq', 2, true);
          public          postgres    false    217            �
           2606    74498    districts districts_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.districts
    ADD CONSTRAINT districts_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.districts DROP CONSTRAINT districts_pkey;
       public            postgres    false    205            �
           2606    74509    houses houses_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.houses
    ADD CONSTRAINT houses_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.houses DROP CONSTRAINT houses_pkey;
       public            postgres    false    207            �
           2606    74547    roles roles_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.roles DROP CONSTRAINT roles_pkey;
       public            postgres    false    211            �
           2606    74476    streets streets_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.streets
    ADD CONSTRAINT streets_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.streets DROP CONSTRAINT streets_pkey;
       public            postgres    false    203            �
           2606    74537    tube_samples tube_samples_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.tube_samples
    ADD CONSTRAINT tube_samples_pkey PRIMARY KEY (" id");
 H   ALTER TABLE ONLY public.tube_samples DROP CONSTRAINT tube_samples_pkey;
       public            postgres    false    210            �
           2606    74527    tubes tubes_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.tubes
    ADD CONSTRAINT tubes_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.tubes DROP CONSTRAINT tubes_pkey;
       public            postgres    false    209            �
           2606    74563    user_roles user_roles_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.user_roles
    ADD CONSTRAINT user_roles_pkey PRIMARY KEY (user_id, role_id);
 D   ALTER TABLE ONLY public.user_roles DROP CONSTRAINT user_roles_pkey;
       public            postgres    false    214    214            �
           2606    74558    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    213            �
           2606    74515    houses houses_district_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.houses
    ADD CONSTRAINT houses_district_id_fkey FOREIGN KEY (district_id) REFERENCES public.districts(id) ON UPDATE CASCADE ON DELETE CASCADE;
 H   ALTER TABLE ONLY public.houses DROP CONSTRAINT houses_district_id_fkey;
       public          postgres    false    207    205    2744            �
           2606    74510    houses houses_street_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.houses
    ADD CONSTRAINT houses_street_id_fkey FOREIGN KEY (street_id) REFERENCES public.streets(id) ON UPDATE CASCADE ON DELETE CASCADE;
 F   ALTER TABLE ONLY public.houses DROP CONSTRAINT houses_street_id_fkey;
       public          postgres    false    2742    207    203            �
           2606    74538 &   tube_samples tube_samples_tube_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tube_samples
    ADD CONSTRAINT tube_samples_tube_id_fkey FOREIGN KEY (tube_id) REFERENCES public.tubes(id) ON UPDATE CASCADE ON DELETE CASCADE;
 P   ALTER TABLE ONLY public.tube_samples DROP CONSTRAINT tube_samples_tube_id_fkey;
       public          postgres    false    2748    210    209            �
           2606    74528    tubes tubes_house_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tubes
    ADD CONSTRAINT tubes_house_id_fkey FOREIGN KEY (house_id) REFERENCES public.houses(id) ON UPDATE CASCADE ON DELETE CASCADE;
 C   ALTER TABLE ONLY public.tubes DROP CONSTRAINT tubes_house_id_fkey;
       public          postgres    false    207    2746    209            �
           2606    74569 "   user_roles user_roles_role_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_roles
    ADD CONSTRAINT user_roles_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.roles(id) ON UPDATE CASCADE ON DELETE CASCADE;
 L   ALTER TABLE ONLY public.user_roles DROP CONSTRAINT user_roles_role_id_fkey;
       public          postgres    false    211    2752    214            �
           2606    74564 "   user_roles user_roles_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_roles
    ADD CONSTRAINT user_roles_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON UPDATE CASCADE ON DELETE CASCADE;
 L   ALTER TABLE ONLY public.user_roles DROP CONSTRAINT user_roles_user_id_fkey;
       public          postgres    false    213    214    2754            L      x������ � �      N      x������ � �      R   E   x�3�tLI	-N-�2�tI�I-Is�9�3��S��sR�L@j�R��R�L���\3��҂�"��=... ���      J      x������ � �      Q      x������ � �      P      x������ � �      U      x������ � �      T      x�3�,��/���4����� '	�     