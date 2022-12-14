PGDMP     :    3            
    z            autoservice_new    14.5    14.4 +    ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    16970    autoservice_new    DATABASE     l   CREATE DATABASE autoservice_new WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
    DROP DATABASE autoservice_new;
                postgres    false            ?            1259    16972    application    TABLE     ?   CREATE TABLE public.application (
    id_application integer NOT NULL,
    name text NOT NULL,
    price integer,
    client_id integer,
    emploee_id integer,
    car_id integer
);
    DROP TABLE public.application;
       public         heap    postgres    false            ?            1259    16971    application_id_application_seq    SEQUENCE     ?   CREATE SEQUENCE public.application_id_application_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.application_id_application_seq;
       public          postgres    false    210            ?           0    0    application_id_application_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.application_id_application_seq OWNED BY public.application.id_application;
          public          postgres    false    209            ?            1259    16981    car    TABLE     ?   CREATE TABLE public.car (
    id_car integer NOT NULL,
    name_car character varying(255) NOT NULL,
    model text NOT NULL,
    client_id integer,
    emploee_id integer,
    date_time date,
    quarter integer
);
    DROP TABLE public.car;
       public         heap    postgres    false            ?            1259    16994 
   car_client    TABLE     `   CREATE TABLE public.car_client (
    id_car integer NOT NULL,
    id_client integer NOT NULL
);
    DROP TABLE public.car_client;
       public         heap    postgres    false            ?            1259    16980    car_id_car_seq    SEQUENCE     ?   CREATE SEQUENCE public.car_id_car_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.car_id_car_seq;
       public          postgres    false    212            ?           0    0    car_id_car_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.car_id_car_seq OWNED BY public.car.id_car;
          public          postgres    false    211            ?            1259    16989    client    TABLE     ?   CREATE TABLE public.client (
    id_client integer NOT NULL,
    surname character varying(25) NOT NULL,
    name character varying(25) NOT NULL,
    discount integer
);
    DROP TABLE public.client;
       public         heap    postgres    false            ?            1259    17010    client_application    TABLE     p   CREATE TABLE public.client_application (
    id_client integer NOT NULL,
    id_application integer NOT NULL
);
 &   DROP TABLE public.client_application;
       public         heap    postgres    false            ?            1259    17027    emploee    TABLE     ?   CREATE TABLE public.emploee (
    id_emploee integer NOT NULL,
    surname character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    id_application integer,
    date date
);
    DROP TABLE public.emploee;
       public         heap    postgres    false            ?            1259    17026    emploee_id_emploee_seq    SEQUENCE     ?   CREATE SEQUENCE public.emploee_id_emploee_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.emploee_id_emploee_seq;
       public          postgres    false    217            ?           0    0    emploee_id_emploee_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.emploee_id_emploee_seq OWNED BY public.emploee.id_emploee;
          public          postgres    false    216            ?            1259    17035    empoloee_application    TABLE     s   CREATE TABLE public.empoloee_application (
    id_emploee integer NOT NULL,
    id_application integer NOT NULL
);
 (   DROP TABLE public.empoloee_application;
       public         heap    postgres    false                       2604    16975    application id_application    DEFAULT     ?   ALTER TABLE ONLY public.application ALTER COLUMN id_application SET DEFAULT nextval('public.application_id_application_seq'::regclass);
 I   ALTER TABLE public.application ALTER COLUMN id_application DROP DEFAULT;
       public          postgres    false    210    209    210                       2604    16984 
   car id_car    DEFAULT     h   ALTER TABLE ONLY public.car ALTER COLUMN id_car SET DEFAULT nextval('public.car_id_car_seq'::regclass);
 9   ALTER TABLE public.car ALTER COLUMN id_car DROP DEFAULT;
       public          postgres    false    211    212    212                       2604    17030    emploee id_emploee    DEFAULT     x   ALTER TABLE ONLY public.emploee ALTER COLUMN id_emploee SET DEFAULT nextval('public.emploee_id_emploee_seq'::regclass);
 A   ALTER TABLE public.emploee ALTER COLUMN id_emploee DROP DEFAULT;
       public          postgres    false    217    216    217            ?          0    16972    application 
   TABLE DATA           a   COPY public.application (id_application, name, price, client_id, emploee_id, car_id) FROM stdin;
    public          postgres    false    210   2       ?          0    16981    car 
   TABLE DATA           a   COPY public.car (id_car, name_car, model, client_id, emploee_id, date_time, quarter) FROM stdin;
    public          postgres    false    212   ?2       ?          0    16994 
   car_client 
   TABLE DATA           7   COPY public.car_client (id_car, id_client) FROM stdin;
    public          postgres    false    214   V3       ?          0    16989    client 
   TABLE DATA           D   COPY public.client (id_client, surname, name, discount) FROM stdin;
    public          postgres    false    213   ?3       ?          0    17010    client_application 
   TABLE DATA           G   COPY public.client_application (id_client, id_application) FROM stdin;
    public          postgres    false    215   84       ?          0    17027    emploee 
   TABLE DATA           R   COPY public.emploee (id_emploee, surname, name, id_application, date) FROM stdin;
    public          postgres    false    217   ]4       ?          0    17035    empoloee_application 
   TABLE DATA           J   COPY public.empoloee_application (id_emploee, id_application) FROM stdin;
    public          postgres    false    218   ?4       ?           0    0    application_id_application_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.application_id_application_seq', 1, false);
          public          postgres    false    209            ?           0    0    car_id_car_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.car_id_car_seq', 1, false);
          public          postgres    false    211            ?           0    0    emploee_id_emploee_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.emploee_id_emploee_seq', 1, false);
          public          postgres    false    216            !           2606    16979    application application_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.application
    ADD CONSTRAINT application_pkey PRIMARY KEY (id_application);
 F   ALTER TABLE ONLY public.application DROP CONSTRAINT application_pkey;
       public            postgres    false    210            '           2606    16998    car_client car_client_pkey 
   CONSTRAINT     g   ALTER TABLE ONLY public.car_client
    ADD CONSTRAINT car_client_pkey PRIMARY KEY (id_car, id_client);
 D   ALTER TABLE ONLY public.car_client DROP CONSTRAINT car_client_pkey;
       public            postgres    false    214    214            #           2606    16988    car car_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.car
    ADD CONSTRAINT car_pkey PRIMARY KEY (id_car);
 6   ALTER TABLE ONLY public.car DROP CONSTRAINT car_pkey;
       public            postgres    false    212            *           2606    17014 *   client_application client_application_pkey 
   CONSTRAINT        ALTER TABLE ONLY public.client_application
    ADD CONSTRAINT client_application_pkey PRIMARY KEY (id_client, id_application);
 T   ALTER TABLE ONLY public.client_application DROP CONSTRAINT client_application_pkey;
       public            postgres    false    215    215            %           2606    16993    client client_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_pkey PRIMARY KEY (id_client);
 <   ALTER TABLE ONLY public.client DROP CONSTRAINT client_pkey;
       public            postgres    false    213            -           2606    17034    emploee emploee_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.emploee
    ADD CONSTRAINT emploee_pkey PRIMARY KEY (id_emploee);
 >   ALTER TABLE ONLY public.emploee DROP CONSTRAINT emploee_pkey;
       public            postgres    false    217            (           1259    16999    idx_car_client__id_client    INDEX     U   CREATE INDEX idx_car_client__id_client ON public.car_client USING btree (id_client);
 -   DROP INDEX public.idx_car_client__id_client;
       public            postgres    false    214            +           1259    17015 &   idx_client_application__id_application    INDEX     o   CREATE INDEX idx_client_application__id_application ON public.client_application USING btree (id_application);
 :   DROP INDEX public.idx_client_application__id_application;
       public            postgres    false    215            .           1259    17040 (   idx_empoloee_application__id_application    INDEX     s   CREATE INDEX idx_empoloee_application__id_application ON public.empoloee_application USING btree (id_application);
 <   DROP INDEX public.idx_empoloee_application__id_application;
       public            postgres    false    218            /           2606    17000     car_client fk_car_client__id_car    FK CONSTRAINT     ?   ALTER TABLE ONLY public.car_client
    ADD CONSTRAINT fk_car_client__id_car FOREIGN KEY (id_car) REFERENCES public.car(id_car) ON DELETE CASCADE;
 J   ALTER TABLE ONLY public.car_client DROP CONSTRAINT fk_car_client__id_car;
       public          postgres    false    3107    212    214            0           2606    17005 #   car_client fk_car_client__id_client    FK CONSTRAINT     ?   ALTER TABLE ONLY public.car_client
    ADD CONSTRAINT fk_car_client__id_client FOREIGN KEY (id_client) REFERENCES public.client(id_client) ON DELETE CASCADE;
 M   ALTER TABLE ONLY public.car_client DROP CONSTRAINT fk_car_client__id_client;
       public          postgres    false    213    214    3109            1           2606    17016 8   client_application fk_client_application__id_application    FK CONSTRAINT     ?   ALTER TABLE ONLY public.client_application
    ADD CONSTRAINT fk_client_application__id_application FOREIGN KEY (id_application) REFERENCES public.application(id_application) ON DELETE CASCADE;
 b   ALTER TABLE ONLY public.client_application DROP CONSTRAINT fk_client_application__id_application;
       public          postgres    false    215    210    3105            2           2606    17021 3   client_application fk_client_application__id_client    FK CONSTRAINT     ?   ALTER TABLE ONLY public.client_application
    ADD CONSTRAINT fk_client_application__id_client FOREIGN KEY (id_client) REFERENCES public.client(id_client) ON DELETE CASCADE;
 ]   ALTER TABLE ONLY public.client_application DROP CONSTRAINT fk_client_application__id_client;
       public          postgres    false    213    3109    215            ?   b   x?M?I
A??_?v??"???w?b0?E!???eb?*??I\??9IH?D;?$Iɛ????ga?r?أ\?l?Q^?\???Ga:ڧ??7???'       ?   ?   x?M??
?0Dϓ?d7M?
?PE????C???փoҖ({?˼?!????ʾ?C3?°b?*????h<?M?3#'uD:?????#?^??$??;:??^?yd?,???o#?]??N6+ɂE>?R?t??3n&e??????)????+?[=N.is??~z^^u??;????!?? <?      ?   /   x???  ??N1?@.z??:???&æ???????&~???;????      ?   ?   x?U˻?@????S?FQԖ???@(??(? 3f/$??.??)??????????d??Ȃ[$6??vD?o]P?6????h]?/+(&=I?????}???{?QѠ3?I??q?h?Zu???ي}?x@?.?;;;????Ƙ?>5?      ?      x?3?4?2?4?????? ??      ?   B   x?3??IM????4?4202?54?50?2???????4????r???sCE?u??b???? ?      ?      x?3?4?2?4?????? ??     