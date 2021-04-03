--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

-- Started on 2021-04-02 21:37:30

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 200 (class 1259 OID 16594)
-- Name: categoria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categoria (
    id integer NOT NULL,
    descricao character varying(200) NOT NULL
);


ALTER TABLE public.categoria OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 16597)
-- Name: Categoria_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.categoria ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Categoria_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 202 (class 1259 OID 16599)
-- Name: designer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.designer (
    id integer NOT NULL,
    nome character varying(100) NOT NULL
);


ALTER TABLE public.designer OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16602)
-- Name: Designer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.designer ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Designer_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 204 (class 1259 OID 16604)
-- Name: jogo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jogo (
    id integer NOT NULL,
    idade integer NOT NULL,
    nome character varying(100) NOT NULL,
    tempo integer NOT NULL,
    jogadoresmin integer NOT NULL,
    jogadoresmax integer,
    idtipo integer NOT NULL
);


ALTER TABLE public.jogo OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16607)
-- Name: Jogo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.jogo ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Jogo_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 206 (class 1259 OID 16609)
-- Name: mecanica; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mecanica (
    id integer NOT NULL,
    descricao character varying(50) NOT NULL
);


ALTER TABLE public.mecanica OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 16612)
-- Name: Mecanica_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.mecanica ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Mecanica_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 208 (class 1259 OID 16614)
-- Name: tipo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo (
    id integer NOT NULL,
    descricao character varying(50) NOT NULL
);


ALTER TABLE public.tipo OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16617)
-- Name: Tipo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.tipo ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Tipo_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 210 (class 1259 OID 16619)
-- Name: jogo-categoria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."jogo-categoria" (
    "idCategoria" integer NOT NULL,
    "idJogo" integer NOT NULL
);


ALTER TABLE public."jogo-categoria" OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 16622)
-- Name: jogo-designer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."jogo-designer" (
    id_jogo integer NOT NULL,
    id_designer integer NOT NULL
);


ALTER TABLE public."jogo-designer" OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 16625)
-- Name: jogo-mecanica; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."jogo-mecanica" (
    "idJogo" integer NOT NULL,
    "idMecanica" integer NOT NULL
);


ALTER TABLE public."jogo-mecanica" OWNER TO postgres;

--
-- TOC entry 3040 (class 0 OID 16594)
-- Dependencies: 200
-- Data for Name: categoria; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.categoria OVERRIDING SYSTEM VALUE VALUES (1, 'humor');
INSERT INTO public.categoria OVERRIDING SYSTEM VALUE VALUES (2, 'luta');
INSERT INTO public.categoria OVERRIDING SYSTEM VALUE VALUES (3, 'fantasia');
INSERT INTO public.categoria OVERRIDING SYSTEM VALUE VALUES (4, 'historia');


--
-- TOC entry 3042 (class 0 OID 16599)
-- Dependencies: 202
-- Data for Name: designer; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.designer OVERRIDING SYSTEM VALUE VALUES (1, 'Steve Jackson');
INSERT INTO public.designer OVERRIDING SYSTEM VALUE VALUES (2, 'Seiji Kanai');


--
-- TOC entry 3044 (class 0 OID 16604)
-- Dependencies: 204
-- Data for Name: jogo; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.jogo OVERRIDING SYSTEM VALUE VALUES (1, 10, 'Munchkin', 90, 3, 6, 1);
INSERT INTO public.jogo OVERRIDING SYSTEM VALUE VALUES (2, 10, 'Love Letter', 20, 2, 4, 1);


--
-- TOC entry 3050 (class 0 OID 16619)
-- Dependencies: 210
-- Data for Name: jogo-categoria; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."jogo-categoria" VALUES (1, 1);
INSERT INTO public."jogo-categoria" VALUES (2, 1);
INSERT INTO public."jogo-categoria" VALUES (3, 1);
INSERT INTO public."jogo-categoria" VALUES (4, 2);


--
-- TOC entry 3051 (class 0 OID 16622)
-- Dependencies: 211
-- Data for Name: jogo-designer; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."jogo-designer" VALUES (1, 1);
INSERT INTO public."jogo-designer" VALUES (2, 2);


--
-- TOC entry 3052 (class 0 OID 16625)
-- Dependencies: 212
-- Data for Name: jogo-mecanica; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."jogo-mecanica" VALUES (1, 1);
INSERT INTO public."jogo-mecanica" VALUES (1, 2);
INSERT INTO public."jogo-mecanica" VALUES (1, 3);
INSERT INTO public."jogo-mecanica" VALUES (2, 1);
INSERT INTO public."jogo-mecanica" VALUES (2, 6);
INSERT INTO public."jogo-mecanica" VALUES (2, 4);
INSERT INTO public."jogo-mecanica" VALUES (2, 5);


--
-- TOC entry 3046 (class 0 OID 16609)
-- Dependencies: 206
-- Data for Name: mecanica; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.mecanica OVERRIDING SYSTEM VALUE VALUES (1, 'Gestao de mao');
INSERT INTO public.mecanica OVERRIDING SYSTEM VALUE VALUES (2, 'rolagem de dados');
INSERT INTO public.mecanica OVERRIDING SYSTEM VALUE VALUES (3, 'selecao de cartas');
INSERT INTO public.mecanica OVERRIDING SYSTEM VALUE VALUES (4, 'blefe');
INSERT INTO public.mecanica OVERRIDING SYSTEM VALUE VALUES (5, 'deducao');
INSERT INTO public.mecanica OVERRIDING SYSTEM VALUE VALUES (6, 'eliminacao de jogadores');


--
-- TOC entry 3048 (class 0 OID 16614)
-- Dependencies: 208
-- Data for Name: tipo; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tipo OVERRIDING SYSTEM VALUE VALUES (1, 'cartas');
INSERT INTO public.tipo OVERRIDING SYSTEM VALUE VALUES (2, 'tabuleiro');


--
-- TOC entry 3058 (class 0 OID 0)
-- Dependencies: 201
-- Name: Categoria_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Categoria_id_seq"', 4, true);


--
-- TOC entry 3059 (class 0 OID 0)
-- Dependencies: 203
-- Name: Designer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Designer_id_seq"', 2, true);


--
-- TOC entry 3060 (class 0 OID 0)
-- Dependencies: 205
-- Name: Jogo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Jogo_id_seq"', 2, true);


--
-- TOC entry 3061 (class 0 OID 0)
-- Dependencies: 207
-- Name: Mecanica_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Mecanica_id_seq"', 6, true);


--
-- TOC entry 3062 (class 0 OID 0)
-- Dependencies: 209
-- Name: Tipo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Tipo_id_seq"', 2, true);


--
-- TOC entry 2887 (class 2606 OID 16629)
-- Name: categoria Categoria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria
    ADD CONSTRAINT "Categoria_pkey" PRIMARY KEY (id);


--
-- TOC entry 2889 (class 2606 OID 16631)
-- Name: designer Designer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.designer
    ADD CONSTRAINT "Designer_pkey" PRIMARY KEY (id);


--
-- TOC entry 2898 (class 2606 OID 16633)
-- Name: jogo-categoria Jogo-Categoria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."jogo-categoria"
    ADD CONSTRAINT "Jogo-Categoria_pkey" PRIMARY KEY ("idJogo", "idCategoria");


--
-- TOC entry 2900 (class 2606 OID 16635)
-- Name: jogo-designer Jogo-Designer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."jogo-designer"
    ADD CONSTRAINT "Jogo-Designer_pkey" PRIMARY KEY (id_jogo, id_designer);


--
-- TOC entry 2902 (class 2606 OID 16637)
-- Name: jogo-mecanica Jogo-Mecanica_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."jogo-mecanica"
    ADD CONSTRAINT "Jogo-Mecanica_pkey" PRIMARY KEY ("idMecanica", "idJogo");


--
-- TOC entry 2891 (class 2606 OID 16639)
-- Name: jogo Jogo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogo
    ADD CONSTRAINT "Jogo_pkey" PRIMARY KEY (id);


--
-- TOC entry 2894 (class 2606 OID 16641)
-- Name: mecanica Mecanica_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mecanica
    ADD CONSTRAINT "Mecanica_pkey" PRIMARY KEY (id);


--
-- TOC entry 2896 (class 2606 OID 16643)
-- Name: tipo Tipo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo
    ADD CONSTRAINT "Tipo_pkey" PRIMARY KEY (id);


--
-- TOC entry 2892 (class 1259 OID 16644)
-- Name: fki_tipo_fk; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_tipo_fk ON public.jogo USING btree (idtipo);


--
-- TOC entry 2904 (class 2606 OID 16645)
-- Name: jogo-categoria categoria_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."jogo-categoria"
    ADD CONSTRAINT categoria_fk FOREIGN KEY ("idCategoria") REFERENCES public.categoria(id);


--
-- TOC entry 2906 (class 2606 OID 16650)
-- Name: jogo-designer designer_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."jogo-designer"
    ADD CONSTRAINT designer_fk FOREIGN KEY (id_designer) REFERENCES public.designer(id);


--
-- TOC entry 2907 (class 2606 OID 16655)
-- Name: jogo-designer jogo_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."jogo-designer"
    ADD CONSTRAINT jogo_fk FOREIGN KEY (id_jogo) REFERENCES public.jogo(id);


--
-- TOC entry 2905 (class 2606 OID 16660)
-- Name: jogo-categoria jogo_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."jogo-categoria"
    ADD CONSTRAINT jogo_fk FOREIGN KEY ("idJogo") REFERENCES public.jogo(id);


--
-- TOC entry 2908 (class 2606 OID 16665)
-- Name: jogo-mecanica jogo_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."jogo-mecanica"
    ADD CONSTRAINT jogo_fk FOREIGN KEY ("idJogo") REFERENCES public.jogo(id);


--
-- TOC entry 2909 (class 2606 OID 16670)
-- Name: jogo-mecanica mecanica_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."jogo-mecanica"
    ADD CONSTRAINT mecanica_fk FOREIGN KEY ("idMecanica") REFERENCES public.mecanica(id);


--
-- TOC entry 2903 (class 2606 OID 16675)
-- Name: jogo tipo_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogo
    ADD CONSTRAINT tipo_fk FOREIGN KEY (idtipo) REFERENCES public.tipo(id) ON UPDATE CASCADE ON DELETE SET NULL;


-- Completed on 2021-04-02 21:37:30

--
-- PostgreSQL database dump complete
--

